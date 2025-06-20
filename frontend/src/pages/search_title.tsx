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
  // console.log(json)
  return json
};

// 検索結果のデータの型
type ResultItem = {
  title: string;
  issue: string;
  date: string;
  page: string;
  size: string;
  author: string;
};

// 検索結果を表示するための関数
function showResult(data: ResultItem[]) {
  if (data.length == 0) {
    return (
      <table>
        <caption>当てはまるものがありませんでした。</caption>
      </table>
    )
  }
  const showRow = data.map((item, index) => {
    let href_text: string
    if (item.issue >= "360") {
      href_text = `https://www.tsukuba.ac.jp/about/public-newspaper/pdf/${item.issue}.pdf`
    } else {
      href_text = `https://www.tsukuba.ac.jp/about/public-newspaper/${item.issue}.pdf`
    }
    return (
      <tr key={index}>
        <td>{item.issue}</td>
        <td>{item.date}</td>
        <td><a href={href_text} target="blank">{item.title}</a></td>
        <td>{item.page}</td>
        <td>{item.author}</td>
      </tr>
    )
  })
  return (
    <table>
      <caption>検索結果</caption>
      <thead>
        <tr>
          <th>号数</th>
          <th>日付</th>
          <th>記事名</th>
          <th>該当ページ</th>
          <th>執筆者</th>
        </tr>
      </thead>
      <tbody>
        {showRow}
      </tbody>
    </table>
  )
};

// 検索ページ全体
export default function Search_fulltext() {
  const [data, setData] = useState<ResultItem[] | null>(null);
  const [error, setError] = useState< string | null >(null)
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError(null);
    // 
    const form = e.currentTarget;
    const formData = new FormData(form);

    const formJson = {
      keywords: formData.get("keywords") as string,
      sort: formData.get("sort") as string,
      mode: formData.get("mode") as string
    };
    // console.log(formJson);

    try {
      const res = await fetchData(formJson);
      setData(res);
      // console.log(data);
    }
    catch (err) {
      if (err instanceof Error) {
        setError(err.message);
        // console.log(error);
      };
    };
  };

  return (
    <>
      <div className="page_title">
        <h1 className="title">記事名検索</h1>
        <p className="sub_title">新聞ごとの記事名に対する検索を行います</p>
      </div>
      <form method="post" onSubmit={handleSubmit}>
        <input type="hidden" name="mode" value="title" />
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

      {data && showResult(data)}

    </>
  );
};
