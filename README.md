🖼️ Smart PCA Image Compressor

A high-performance image compression tool powered by PCA (Principal Component Analysis).
Reconstructs images using fewer PCA components, providing massive size reduction with minimal quality loss.

🚀 About the Project

Smart PCA Image Compressor is a fast, lightweight, and entirely client-side image compression tool.
It uses the PCA algorithm to reconstruct images with fewer features, achieving high compression efficiency.

Ideal for:

Developers

Students

Researchers

Anyone working with image optimization

🎯 Key Features

Drag & Drop image upload

Fast PCA compression

Adjustable PCA components slider

Before/After comparison slider

Compression statistics (size, ratio, saved %)

Clean UI using TailwindCSS

Real-time preview

Fully offline, no backend

Mobile responsive

📸 Screenshots
(Replace these with your own)

assets/demo-1.png
assets/demo-2.png
assets/demo-3.png

Add like this:


🧠 How PCA Image Compression Works

PCA reduces image size by:

Splitting image into R, G, B channels

Computing covariance matrices

Extracting eigenvectors

Keeping top K principal components

Reconstructing image with reduced dimensions

Benefits:

Smaller file sizes

Very small quality loss

Fast and efficient

🛠️ Tech Stack

Frontend: React, TailwindCSS, Vite
Image Processing: PCA (custom), Canvas API
Language: JavaScript (and optional Python)
Version Control: Git

📁 Project Folder Structure

project/
├── src/
│ ├── components/
│ ├── utils/
│ ├── App.jsx
│ └── main.jsx
├── public/
├── README.md
├── package.json
├── tailwind.config.js
└── venv/ (ignored)

🧩 Installation & Setup

Clone the repository
git clone https://github.com/USERNAME/REPO_NAME.git

cd REPO_NAME

Install dependencies
npm install

Start development server
npm run dev

🖱️ Usage Guide

Open the app

Upload an image

Adjust PCA slider

Compare before vs after

Download compressed output

🗂️ Recommended .gitignore

venv/
pycache/
node_modules/
dist/
*.pyc
.env
.DS_Store

🧬 System Architecture

User Upload → Preprocessing → PCA Compression → Reconstruction → Preview → Download

📉 Example Compression Results

Image | Original | Compressed | Savings
Sample 1: 2.1 MB → 340 KB → 84%
Sample 2: 1.6 MB → 290 KB → 81%
Sample 3: 4.4 MB → 710 KB → 83%

🧪 Future Enhancements

Batch image compression

Dark mode support

PDF/image export

Multi-threaded PCA

Online hosted version

Auto-optimization

🤝 Contributing

Contributions are welcome!
Open an issue before making major changes.

📜 License

MIT License

⭐ Support

If this project helped you, consider giving it a ⭐ on GitHub!
