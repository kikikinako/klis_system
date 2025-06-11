import React, { useState } from "react";
const URL: string = "http://localhost:8000/search";

export default function Main() {
  const [result, setResult] = useState<{ filename: string[]; page: string[] }>({ filename: [], page: [] });

  async function sendData(data: { keywords: string, sort: string }) {
    const response = await fetch(URL, {
      mode: "cors",
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ "keywords": data.keywords, "sort": data.sort })
    });
    const json = await response.json();
    console.log(json);
    setResult({ filename: json.filename, page: json.page });
  }

  function MyForm() {
    function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
      e.preventDefault();
      const form = e.currentTarget;
      const formData = new FormData(form);

      const formJson = {
        keywords: formData.get("keywords") as string,
        sort: formData.get("sort") as string
      };
      console.log(formJson);

      sendData(formJson);
    };
    return (
      <form method="post" onSubmit={handleSubmit}>
        <label>
          Input keywords: <input name="keywords" />
        </label>
        <hr />
        Sort result
        <br />
        <label>
          ascending: <input type="radio" name="sort" value="asc" defaultChecked={true} />
        </label>
        <label>
          descending: <input type="radio" name="sort" value="des" />
        </label>
        <hr />
        <button type="reset">Reset form</button>
        <button type="submit">Submit form</button>
      </form>
    )
  };

  return (
    <>
      <h1>検索用ページの例というか練習</h1>
      <MyForm />
      <hr />
      <h2>検索結果</h2>
      <div>
        <strong>filename:</strong>
        <ul>
          {result.filename.map((f, i) => <li key={i}>{f}</li>)}
        </ul>
        <strong>page:</strong>
        <ul>
          {result.page.map((p, i) => <li key={i}>{p}</li>)}
        </ul>
      </div>
    </>
  );
}
