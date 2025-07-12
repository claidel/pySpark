def generate_html(data):
    date = data["date"]
    jour = data["jour_semaine"]
    total = data["total_journalier"]
    resume = data["resume"]
    lignes = data["donnees"]
    stock_bouchons = data.get("total_bouchons", "N/A")
    stock_etiquettes = data.get("total_etiquettes", "N/A")
    stock_trompettes = data.get("total_trompettes", "N/A")

    html = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Rapport journalier - {date}</title>
  <style>
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #ffffff;
      color: #000;
    }}
    .header {{
      background-color: #3c4c44;
      color: white;
      padding: 40px 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .logo {{
      font-size: 24px;
      font-weight: bold;
      border: 2px solid white;
      padding: 10px 20px;
      border-radius: 50%;
      text-align: center;
    }}
    .company-info {{
      text-align: right;
      font-size: 14px;
    }}
    .reference {{
      padding: 30px;
      font-size: 14px;
      display: flex;
      justify-content: space-between;
    }}
    .table-container {{
      padding: 0 30px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }}
    th, td {{
      padding: 12px;
      border-bottom: 1px solid #ccc;
      text-align: center;
    }}
    th {{
      border-top: 1px solid #ccc;
    }}
    .total {{
      padding: 30px;
      text-align: right;
      font-weight: bold;
      font-size: 18px;
    }}
    .stocks {{
      padding: 0 30px;
      font-size: 14px;
      margin-top: 20px;
      line-height: 1.6em;
    }}
  </style>
</head>
<body>

  <div class="header">
    <div class="logo">DBD<br>SARL</div>
    <div class="company-info">
      <div>Rapport Journalier - Usine</div>
      <div>37, Rue Mombele, C/ Limete</div>
    </div>
  </div>

  <div class="reference">
    <div>
      <div>En référence</div>
      <div>+243828474696</div>
      <div>37, Rue Mombele, C/ Limete</div>
      <div>{jour}</div>
    </div>
    <div>{date}</div>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Tour</th>
          <th>Heure Sortie</th>
          <th>Heure Arrivée</th>
          <th>Nbre de Bidons</th>
          <th>Vendu</th>
          <th>Eau & Défauts</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        {''.join(f'''
          <tr>
            <td>{ligne["tour"]}</td>
            <td>{ligne["heure_sortie"]}</td>
            <td>{ligne["heure_arrivee"]}</td>
            <td>{ligne["bidon_total"]}</td>
            <td>{ligne["bidon_vendu"]}</td>
            <td>{ligne["bidon_eau_defaut"]}</td>
            <td>{ligne["profit_total"]} FC</td>
          </tr>''' for ligne in lignes)}
      </tbody>
    </table>
  </div>

  <div class="stocks">
    <p>📦 <strong>Stock Bouchons :</strong> {stock_bouchons}</p>
    <p>🏷️ <strong>Stock Étiquettes :</strong> {stock_etiquettes}</p>
    <p>🎺 <strong>Stock Trompettes :</strong> {stock_trompettes}</p>
  </div>

  <div class="total">Total : {total} FC</div>

</body>
</html>
"""
    return html
