
import { useState } from "react";

const api = {
  key: "f38cca6e872bdf147280098ae637d674",
  base: "https://api.openweathermap.org/data/2.5/",
};

function App() {
  const [search, setSearch] = useState("");
  const [weather, setWeather] = useState({});

  /*
    Se presiona el botón de búsqueda. Realiza una llamada de búsqueda a la API Open Weather Map.
  */
  const searchPressed = () => {
    fetch(`${api.base}weather?q=${search}&units=metric&APPID=${api.key}&lang=es`)
      .then((res) => res.json())
      .then((result) => {
        setWeather(result);
      });
  };


  
  
  return (
    <body className="text-center bg-[#282c34] h-dvh w-auto overflow-auto">
          {/* Encabezado */}
      <header class= "flex flex-col items-center justify-center  ">
        <div class= " mx-10 my-10 pointer-events-none space-y-4 font-bold tracking-tight text-gray-900 mb-4 uppercase bg-gradient-to-r from-orange-400 to-blue-600 py-4 px-4 rounded">
          <h1 class="text-5xl">Another Weather App</h1>
          <p class='text-xl'> Busca el clima actual de tu ciudad solo buscando en el navegador de aqui abajo</p>
        </div>
        
      </header>

      <section  class= "mx-10 mt-2 mb-1 p-10 gap-15 grid-rows-1">
        {/* Caja */}
          <div class="mx-10 mt-6 mb-10 p-5 flex items-stretch place-content-center " >
            <input
                class= "bg-[#222630] w-80 p-2 mr-5 outline-none w-[280px] text-white rounded-lg border-2 transition-colors duration-100 border-solid focus:border-[#596A95] border-[#2B3040]"
                type="text"
                placeholder="Introduzca el sitio/ciudad..."
                onChange={(e) => setSearch(e.target.value)} 
              />

              <button
                class="p-10 bg-gradient-to-r from-purple-400 to-blue-500 hover:from-pink-500 h-20% hover:to-purple-600 text-white font-bold py-3 px-6 rounded-full shadow-lg transform transition-all duration-500 ease-in-out hover:scale-110 hover:brightness-110 hover:animate-pulse active:animate-bounce"
              onClick={searchPressed}>Buscar</button>
          </div>

          {/* Si el clima no está definido, se muestran los resultados de la API */}
          {typeof weather.main !== "undefined" ? (
            <div class= " flex justify-center items-center space-y-4 drop-shadow-xl  rounded-xl bg-gradient-to-r from-teal-300 to-blue-700 tracking-tight">
              <div class= "mx-10 my-10 p-2">
                {/* Locacion  */}
                <p  className="text-white text-2xl font-bold">{weather.name}</p>

                {/* Temperatura en Celsius  */}
                <p className="text-white text-2xl font-bold">{weather.main.temp}°C</p>

                {/* Condicion (Sunny ) */}
                <p className="text-white text-2xl font-bold">{weather.weather[0].main}</p>
                <p className="text-white text-2xl font-bold">({weather.weather[0].description})</p>
                </div>

              </div>
          ) : ("")}


      </section>
      <footer className="h-auto">
        </footer>    
    </body>
  );
}

export default App;