import './App.css';
import FunctionalComponent from './components/functional';
import ClassComponent from './components/class';

function App() {
  return (
    <div>
      <FunctionalComponent userName="Hemanth"/>
      <ClassComponent userName="Hemanth"/>
    </div>
  );
}

export default App;
