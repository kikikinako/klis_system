

export default function About() {
  return (
    <>
      <div className="page_title">
        <h1 className="title">About</h1>
        <p className="sub_title">システムの概要</p>
      </div>
      <p className="description">
        筑波大学新聞横断検索システムは、筑波大学新聞新聞の本文や見出しを号数をまたいで検索することのできるシステムです。

      </p>
      <div className="paragraph">
        <div className="page_title">
          <h1>使い方</h1>
          <p className="sub_title">それぞれの検索の違いを説明しています</p>
        </div>
        <div className="description">
          <p>
            単語検索では、筑波大学新聞内に含まれる文章を対象として検索を行います。
          </p>
          <p>
            記事名検索では、筑波大学新聞の記事の見出し・小見出しの名前を対象として検索を行います。
          </p>
        </div>
      </div>
      <div className="paragraph">
        <div className="page_title">
          <h1>検索対象外PDF一覧</h1>
          <p className="sub_title">形式が異なるため、検索対象外としたPDFファイルの一覧を表示します。</p>
        </div>
        <div className="description">
          <p>以下のPDFファイルは形式が異なるため、検索対象外としています。</p>
          <ul>
            <li><a href="/irregular_issue">検索対象外PDF一覧</a></li>
          </ul>
        </div>
      </div>
      <div className="paragraph">
        <div className="page_title">
          <h1>システム概要</h1>
          <p className="sub_title">使用言語やフレームワークについて</p>
        </div>
        <div className="description">
          <ul>
            <li>バックエンド：Python(Flask)</li>
            <li>フロントエンド：Typescript(React)</li>
          </ul>
        </div>
      </div>

      <div className="paragraph">
        <div className="page_title">
          <h1>筑波大学新聞</h1>
        </div>
        <div className="description">
          <p>使用させていただいた筑波大学新聞社様へのリンクです</p>
          <ul>
            <li><a href="https://www.tsukuba.ac.jp/about/public-newspaper/">筑波大学新聞</a></li>
          </ul>
        </div>
      </div>

      <div className="paragraph">
        <div className="page_title">
          <h1>作成者</h1>     
        </div>
        <div className="description">
          <p>10班　温泉生卵</p>
        </div>
      </div>
    </>
  )
}