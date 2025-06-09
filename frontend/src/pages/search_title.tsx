import { useState } from "react";


const URL: string = "http://localhost:8000/";

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
}

export default function Search_title() {
  const [data, setData] = useState<{ "result" : string }[] | null>(null)
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

  const Listitems = data && data.map(item => <li>{item}</li>)
  
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

      <ul>{Listitems}</ul>

    </>
  );
}
