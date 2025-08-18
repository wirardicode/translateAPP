const api_key = 'hkbsafwoyusdhblb12hblflhb5';

        async function ocr() {
            const fileInput = document.getElementById("fileInput");
            const ocrResult = document.getElementById("ocrResult");
            const translateResult = document.getElementById("translateResult");
            const uploadBtn = document.getElementById("uploadBtn");

            if (!fileInput.files.length) {
                alert("Pilih file gambar dulu!");
                return;
            }

            const formData = new FormData();
            formData.append("file", fileInput.files[0]);

            uploadBtn.disabled = true;
            uploadBtn.textContent = "PROCESSING...";

            ocrResult.innerHTML = '<span class="loading-text">Memproses OCR... █▓▒░</span>';
            translateResult.innerHTML = '<span class="loading-text">Waiting for OCR... █▓▒░</span>';

            try {
                const response = await fetch("http://127.0.0.1:8000/imgeOCR", {
                    method: "POST",
                    body: formData,
                    headers: {
                        "Authorization": "Bearer " + api_key
                    }
                });

                const data = await response.json();
                ocrResult.innerHTML = `<span class="success-text">█ OCR COMPLETE █</span><br><br>Hasil OCR:<br>${data.message}`;

                translate(data.message);

                uploadBtn.disabled = false;
                uploadBtn.textContent = "PROSES OCR";
            } catch (error) {
                ocrResult.innerHTML = '<span class="error-text">█ ERROR █ Terjadi kesalahan saat OCR!</span>';
                translateResult.innerHTML = '<span class="error-text">█ TRANSLATION CANCELLED █</span>';
                uploadBtn.disabled = false;
                uploadBtn.textContent = "PROSES OCR";
            }
        }

        async function translate(text) {
            const translateResult = document.getElementById("translateResult");
            const lang = document.getElementById("languageSelect").value;
            
            translateResult.innerHTML = '<span class="loading-text">Translating... █▓▒░</span>';

            try {
                const response = await fetch("http://127.0.0.1:8000/translate", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        source: "auto",
                        target: lang,
                        text: text,
                        proxies: []
                    })
                });

                const data = await response.json();
                const translated = (data.translation || JSON.stringify(data)).replace(/\n/g, "<br>");

                translateResult.innerHTML =
                    `<span class="success-text">█ TRANSLATION COMPLETE █</span><br><br>Hasil Translate:<br>${translated}`;

            } catch (err) {
                console.error(err);
                translateResult.innerHTML =
                    '<span class="error-text">█ ERROR █ Gagal translate!</span>';
            }
        }


        document.getElementById("uploadBtn").addEventListener("click", ocr);