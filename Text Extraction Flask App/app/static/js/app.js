const { createWorker } = Tesseract;

const fileInput = document.getElementById('fileInput');
const extractBtn = document.getElementById('extractBtn');
const resultDiv = document.getElementById('result');

extractBtn.addEventListener('click', async () => {
    const worker = createWorker();

    await worker.load();
    await worker.loadLanguage('eng');
    await worker.initialize('eng');

    const image = fileInput.files[0];
    const { data: { text } } = await worker.recognize(image);

    resultDiv.innerHTML = `<h2>Extracted Text:</h2><p>${text}</p>`;

    await worker.terminate();
});




import { useEffect, useState } from "react";
import { createWorker } from "tesseract.js";
import "./App.css":
function App() {
    const [ocr, setOcr] = useState("");
    cont [imageData, setImageData] = useState(null);
    const worker = createWorker({
        logger: (m) => {
            console.log(m);
        },
    });
    const convertImageToText = async () => {
        if (!imageData) return;
        await worker.load();
        await worker.loadLanguage("eng");
        await workerinitialize("eng");
        const{
            data: { text },
        } = await worker.recognize(imageData);
        setOcr(text);
    };
    useEffect(() => {
        convertImageToText();
    }, [imageData]);

    function handleImageChange(e) {
        const file = e.target.files[0];
        if(!file)return;
        const reader = new FileReader();
        reader.onloadend = () => {
            const imageDataUri = reader.result;
            console.log({ imageDataUri });
            setImageData(imageDataUri);
        };
        reader.readAsDataURL(file);
    }
    return (
        <
    )
}