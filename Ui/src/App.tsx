import { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");

  const handleSubmit = async (e: { preventDefault: () => void }) => {
    e.preventDefault();
    try {
      const response = await fetch(
        "/api/url/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ 'original_url': url }),
        }
      );
      const data = await response.json();
      setShortUrl(data.full_short_url);
    } catch (error) {
      console.error("Error shortening URL:", error);
    }
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="flex flex-col justify-center items-center">
        <div className="w-100">
          <h1 className="text-lg text-left font-semibold">Alamat URL</h1>
        </div>
        <form className="flex w-100" onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Masukkan URL yang akan diproses"
            className="mr-2 p-2 border rounded w-full"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
          <button
            type="submit"
            className="py-1 px-3 bg-blue-500 text-white rounded-full w-3/6"
          >
            <i className="bi bi-floppy me-2"></i>
            <span>Simpan</span>
          </button>
        </form>
        {shortUrl && (
          <div className="mt-4 w-100">
            <h2 className="text-lg font-semibold">Shortened URL:</h2>
            <a href={shortUrl} className="text-blue-500">
              {shortUrl}
            </a>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
