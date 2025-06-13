export default function IrregularIssue() {
  const excludedPdfs = [
     244, 245, 246, 
  ];

  return (
    <div>
      <h2>検索対象外PDF一覧</h2>
      <p>以下のPDFファイルは形式が異なるため、検索対象外としています。</p>
      <table>
        <thead>
          <tr>
            <th>ファイル名</th>
          </tr>
        </thead>
        <tbody>
          {excludedPdfs.map(num => (
            <tr key={num}>
                <td>
                    <a href={`https://www.tsukuba.ac.jp/about/public-newspaper/${num}.pdf`} target="_blank" rel="noopener noreferrer">
                    筑波大学新聞{num}号
                    </a>
                </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}