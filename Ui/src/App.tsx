function App() {
  return (
    <div className="flex justify-center items-center h-screen">
      <div className="flex flex-col justify-center items-center">
        <div className="w-100">
          <h1 className="text-lg text-left font-semibold">Alamat URL</h1>
        </div>
        <form className="flex w-100">
          <input type="text" placeholder="Masukkan URL yang akan diproses" className="mr-2 p-2 border rounded w-full" />
          <button type="submit" className="py-1 px-3 bg-blue-500 text-white rounded-full w-3/6">
            <i className="bi bi-floppy me-2"></i>
            <span>Simpan</span>
          </button>
        </form>
      </div>
    </div>
  );
}

export default App;
