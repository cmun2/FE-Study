import { useEffect } from "react";
const App = () => {
  useEffect(() => {
    console.log(1);
  }, []);
  return (
    <div className="App">
      <h1>useEffect 순서 테스트</h1>
      <FirstBox />
    </div>
  );
};

const FirstBox = () => {
  useEffect(() => {
    console.log(2);
  }, []);
  return (
    <>
      <h2>FirstBox</h2>
      <SecondBox />
    </>
  );
};

const SecondBox = () => {
  useEffect(() => {
    console.log(3);
  }, []);
  return <h2>SecondBox</h2>;
};

export default App;
