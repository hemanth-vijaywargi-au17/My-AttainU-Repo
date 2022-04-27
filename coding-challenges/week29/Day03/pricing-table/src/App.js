import planInfo from './components/planInfo';
import PlanBox from './components/PlanBox';
import './components/styles.css'

const priceComponents = planInfo.map(info => {
  return <PlanBox planInfo={info} />
})

function App() {
  return (
    <div id="main-box">
      <h1>Pricing Table</h1>
      <div id="price-parent">
        {priceComponents}
      </div>
    </div>
  );
}

export default App;
