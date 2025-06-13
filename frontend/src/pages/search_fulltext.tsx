import { useState } from "react";

const URL: string = import.meta.env.VITE_API_BASE_URL;

// 検索キーワードの送信とデータの取得
async function fetchData (data: { keywords: string, sort: string, mode: string}) {
  const res = await fetch(`${URL}/search`, {
    mode: "cors",
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({"keywords": data.keywords, "sort": data.sort, "mode": data.mode})
  });
  if (!res.ok) {
    throw new Error(`HTTP error! status: ${res.status}`);
  };
  const json = await res.json();
  return json
};

// 検索結果のデータの型
type ResultItem = {
  filename: string;
  page: number[];
  matched_keywords: string[];
};

function showResult(
  data: ResultItem[],
  filterWord: string | null,
  setFilterWord: (w: string | null) => void
) {
  if (data.length == 0) {
    return (
      <table>
        <caption>当てはまるものがありませんでした。</caption>
      </table>
    )
  }

  const allKeywords = Array.from(
    new Set(data.flatMap(item => item.matched_keywords))
  );

  // 単語ごとに出現したファイル一覧を作成
  const wordToFiles: { [word: string]: string[] } = {};
  data.forEach(item => {
    item.matched_keywords.forEach(word => {
      if (!wordToFiles[word]) wordToFiles[word] = [];
      wordToFiles[word].push(item.filename);
    });
  });

  // フィルタ適用
  const filteredData = filterWord
    ? data.filter(item => item.matched_keywords.includes(filterWord))
    : data;

  const showRow = filteredData.map((item, index) => {
    let href_text: string
    if (item.filename >= "360") {
      href_text = `https://www.tsukuba.ac.jp/about/public-newspaper/pdf/${item.filename}.pdf`
    } else {
      href_text = `https://www.tsukuba.ac.jp/about/public-newspaper/${item.filename}.pdf`
    }
    return (
      <tr key={index}>
        <td><a href={href_text} target="blank">{item.filename}</a></td>
        <td>{item.page.join(", ")}</td>
      </tr>
    )
  })

  return (
    <>
      <div style={{ margin: "1em 0", fontWeight: "bold" }}>
        ヒット件数: {filteredData.length}　
      </div>
      <div style={{ margin: "1em 0", fontWeight: "bold" }}>
        ヒットした単語一覧:{" "}
        {allKeywords.map(word => (
          <span
            key={word}
            style={{
              cursor: "pointer",
              color: filterWord === word ? "blue" : "black",
              textDecoration: "underline",
              marginRight: "0.5em"
            }}
            onClick={() => setFilterWord(filterWord === word ? null : word)}
          >
            {word}
          </span>
        ))}
        {filterWord && (
          <button style={{ marginLeft: "1em" }} onClick={() => setFilterWord(null)}>
            クリア
          </button>
        )}
      </div>
      <div style={{ margin: "1em 0" }}>
      </div>
      <table>
        <caption>検索結果</caption>
        <thead>
          <tr>
            <th>号数</th>
            <th>該当ページ</th>
          </tr>
        </thead>
        <tbody>
          {showRow}
        </tbody>
      </table>
    </>
  )
}

// 検索ページ全体
export default function Search_fulltext() {
  const [data, setData] = useState<ResultItem[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [filterWord, setFilterWord] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError(null);
    setFilterWord(null);
    const form = e.currentTarget;
    const formData = new FormData(form);

    const formJson = {
      keywords: formData.get("keywords") as string,
      sort: formData.get("sort") as string,
      mode: formData.get("mode") as string
    };

    try {
      const res = await fetchData(formJson);
      setData(res);
    }
    catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      };
    };
  };

  return (
    <>
      <div className="page_title">
        <h1 className="title">単語検索</h1>
        <p className="sub_title">新聞全体に対する単語検索を行います</p>
      </div>
      <form method="post" onSubmit={handleSubmit}>
        <input type="hidden" name="mode" value="fulltext" />
        <label>
          <p>検索キーワード</p>
          <input name="keywords" className="text-input" required/>
        </label>
        <hr />
        <p>並び替え</p>
        <div className="radio-group" >
          <label>
            昇順（古い順）：<input type="radio" name="sort" value="asc" />
          </label>
          <label>
            降順（新しい順）：<input type="radio" name="sort" value="des" defaultChecked />
          </label>
        </div>
        <hr />
        <button type="reset">空にする</button>
        <button type="submit">検索する</button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {data && showResult(data, filterWord, setFilterWord)}

    </>
  );
};