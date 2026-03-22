import Header from "./components/layout/Header";
import Map from "./components/map/Map";
import "./App.scss";

function App() {
  return (
    <div className="app">
      <Header />

      <main className="app__main">
        <Map />
      </main>
    </div>
  );
}

export default App;
