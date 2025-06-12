import { NavLink } from "react-router-dom";


export default function Home() {
  return (  
    <>
      <div className="home-top">
        <div className="page_title">
          <h1 className="title">筑波大学新聞横断検索システム</h1>
        </div>
      </div>
      <div className="home-menu-wrapper">
        <div className="home-menu">
          <div id="home-menu1">
            <h1><NavLink to={"search_fulltext"}>全文検索</NavLink></h1>
            <p>　新聞記事全体を対象とした検索を行います。</p>
          </div>
          <div id="home-menu2">
            <h1><NavLink to={"search_title"}>記事名検索</NavLink></h1>
            <p>　それぞれの新聞の記事名・見出しを対象として検索を行います。</p>
          </div>
          <div id="home-menu3"></div>
          <div id="home-menu4">
            <h1><NavLink to={"about"}>ABOUT</NavLink></h1>
            <p>　システムの概要や使い方について記載しています。</p>
          </div>
          <div id="home-menu5"></div>
          <div id="home-menu6"></div>
        </div>
      </div>
    </>
  )
}