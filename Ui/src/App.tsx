function App() {
  return (
    <div className="flex justify-center items-center h-screen">
      <div className="flex flex-col justify-center items-center">
        <div className="mb-4 w-100">
          <h1 className="text-lg text-left font-semibold">Masukkan alamat URL yang ingin dipendekkan</h1>
        </div>
        <form className="flex w-100">
          <input type="text" placeholder="Enter URL" className="mr-2 p-2 border rounded w-full" />
          <button type="submit" className="p-2 bg-blue-500 text-white rounded">Simpan</button>
        </form>
      </div>
    </div>
  );
}

export default App;
