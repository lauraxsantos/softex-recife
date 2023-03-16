import logo from './logo.svg';
import './App.css';
import Name from './components/name';
import Layout from './components/props';
function App() {
  return (
    <div className="App">
      <Layout>
        <Name/>
      </Layout>
    </div>
  );
}

export default App;
