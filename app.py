from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    biaya = None
    if request.method == "POST":
        try:
            # Ambil input dari form
            jarak = float(request.form.get("jarak"))
            konsumsi_bbm = float(request.form.get("konsumsi_bbm"))
            harga_bbm = float(request.form.get("harga_bbm"))

            # Hitung biaya perjalanan
            total_liter = jarak / konsumsi_bbm
            biaya = total_liter * harga_bbm
        except ValueError:
            biaya = "Input tidak valid. Harap masukkan angka yang benar."

    return render_template("index.html", biaya=biaya)

if __name__ == "__main__":
    app.run(debug=True)