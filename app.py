@app.route("/generate", methods=["POST"])
def generate_pdf():
    data = request.json

    if not data:
        return {"error": "No data provided"}, 400

    # Ajouter les champs manquants si absents
    date_actuelle = datetime.now()
    data.setdefault("date", date_actuelle.strftime("%Y-%m-%d"))
    data.setdefault("jour_semaine", date_actuelle.strftime("%A"))
    data.setdefault("total_journalier", sum(l.get("profit_total", 0) for l in data.get("donnees", [])))
    data.setdefault("total_bouchons", 0)
    data.setdefault("total_etiquettes", 0)
    data.setdefault("total_trompettes", 0)

    rendered = render_template("rapport.html", **data)
    filename = f"rapport_{date_actuelle.strftime('%Y%m%d_%H%M%S')}.pdf"
    output_path = f"/tmp/{filename}"

    pdfkit.from_string(rendered, output_path)
    return send_file(output_path, as_attachment=True, download_name=filename)
