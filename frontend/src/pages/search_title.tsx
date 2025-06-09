import { useState } from "react";


const URL: string = "http://localhost:8000/";

// 検索キーワードの送信とデータの取得
async function fetchData (data: { keywords: string, sort: string }) {
  const res = await fetch(`${URL}/search`, {
    mode: "cors",
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({"keywords": data.keywords, "sort": data.sort})
  });
  if (!res.ok) {
    throw new Error(`HTTP error! status: ${res.status}`);
  };
  const json = await res.json();
  console.log(json["result"]);
  return json.result
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
  const showRow = data.map((item, index) => {
    return (
      <tr key={index}>
        <td>{item.title}</td>
        <td>{item.issue}</td>
        <td>{item.date}</td>
        <td>{item.page}</td>
        <td>{item.size}</td>
        <td>{item.author}</td>
      </tr>
    )
  })
  return (
    <table>
      <thead>
        <tr>
          <th></th>
        </tr>
      </thead>
      <tbody>
        {showRow}
      </tbody>
    </table>
  )
};

// 検索ページ全体
export default function Search_title() {
  const [data, setData] = useState<ResultItem[] | null>(null);
  const [error, setError] = useState< string | null >(null)
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // 
    const form = e.currentTarget;
    const formData = new FormData(form);

    const formJson = {
      keywords: formData.get("keywords") as string,
      sort: formData.get("sort") as string
    };
    console.log(formJson);

    try {
      const res = await fetchData(formJson);
      setData(res);
      console.log(data);
    }
    catch (err) {
      if (err instanceof Error) {
        setError(err.message);
        console.log(error);
      };
    };
  };

  
  return (
    <>
      <h1>全文検索</h1>
      <form method="post" onSubmit={handleSubmit}>
        <label>
          Input keywords: <input name="keywords" />
        </label>
        <hr />
        Sort result
        <br />
        <label>
          ascending: <input type="radio" name="sort" value="asc" defaultChecked={true}/>
        </label>
        <label>
          descending: <input type="radio" name="sort" value="des" />
        </label>
        <hr />
        <button type="reset">Reset form</button>
        <button type="submit">Submit form</button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {data && showResult(data)}

    </>
  );
};
