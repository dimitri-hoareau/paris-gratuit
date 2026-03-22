import Header from "./components/layout/Header";
import "./App.scss";

function App() {
  return (
    <div className="app">
      <Header />

      <main className="app__main">
        <p>La carte Leaflet ira ici</p>
      </main>
    </div>
  );
}

export default App;
