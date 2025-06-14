# 筑波大学新聞横断検索システム

本システムは、筑波大学 知識情報・図書館学類のシステム主専攻実習において開発された、学内新聞記事の横断検索を目的としたシステムである。

## 使用技術

- バックエンド：Flask（Python）＋ SQLite3  
- フロントエンド：React（TypeScript）、CSS  
- 実行環境：ローカル環境またはLinuxサーバ上でのデプロイ

## システム概要

本システムは、筑波大学新聞の本文および見出しに対して、号をまたいだ横断的な検索を可能にするWebアプリケーションである。  
検索機能は「単語検索」と「記事名検索」の2種類を提供し、それぞれ以下の内容を対象としている。

- 単語検索：筑波大学新聞に含まれる本文中の単語を対象とした全文検索  
- 記事名検索：記事の見出し・小見出しを対象とした検索  

また、PDFファイルの中には構造が特殊で検索対象外としたものが存在し、それらは「検索対象外PDF一覧」として別ページにまとめて表示している。

学内の新聞アーカイブ活用を促進し、過去の記事情報への容易なアクセスを実現することを目的としている。

## チーム体制と役割分担

| 氏名           | 役割                             | 主な担当内容 |
|----------------|----------------------------------|----------------|
| 浅野 怜矢       | プロジェクト推進・外部連携          | アイデア出し、スライド作成、筑波大学新聞など外部との連絡 |
| kinako       | フロントエンド開発                  | React（TypeScript）およびCSSによるUI設計と実装 |
| 鈴木 史麿       | バックエンド・フロントエンド・データ処理 | PDFデータの解析、データベース、フロントエンド・バックエンド両方の機能改善 |
| CHEN XINZHE    | バックエンド開発                    | SQLite3を用いたデータベース設計とPythonによる検索機能の実装 |

---

# Tsukuba University News Digitization Search System

This system was developed as part of a major course project at the University of Tsukuba to enable cross-issue search of campus newspaper articles.

## Technologies Used

- Backend: Flask (Python) + SQLite3  
- Frontend: React (TypeScript), CSS  
- Deployment: Localhost / Ubuntu Linux

## Project Overview

This web application enables cross-issue keyword search over the articles and headlines of the Tsukuba University Newspaper.  
It provides two types of search functionality:

- **Word Search**: Full-text search across all article bodies within the newspaper archive  
- **Title Search**: Search targeting headlines and subheadings of articles  

Certain PDF files were excluded from the search due to incompatible structure; these are listed on a dedicated “Excluded PDFs” page.

The system aims to promote the use of on-campus newspaper archives and facilitate easier access to past article information.

## Team Structure and Role Breakdown

| Name             | Role                            | Contributions |
|------------------|----------------------------------|----------------|
| Reiya Asano      | Project Lead & Liaison          | Proposed core ideas, created slides, and handled external communication (e.g., Tsukuba University Newspaper) |
| Xinzhe Chen      | Backend Developer               | Designed and implemented the search functionality using Python and SQLite3 |
| Fumimaro Suzuki  | Backend / Frontend Engineer     | Parsed raw PDF data, contributed to database schema design, and improved both backend and frontend features |
| Kinako      | Frontend Developer              | Built the user interface using React (TypeScript) and styled it with CSS |
