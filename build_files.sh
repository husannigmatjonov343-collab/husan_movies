#!/bin/bash
# Vercel deploy paytida ishga tushadigan build skripti
set -e

echo "Bog'liqliklar o'rnatilmoqda..."
pip install -r requirements.txt

echo "Ma'lumotlar bazasi tayyorlanmoqda..."
python -m app.seed

echo "Build muvaffaqiyatli yakunlandi."
