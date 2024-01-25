import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Edit from "./pages/Edit";
import New from "./pages/New";
import Diary from "./pages/Diary";

// components
import Mybutton from "./components/Mybutton";
import MyHeader from "./components/MyHeader";

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <MyHeader
                    headText={"App"}
                    leftChild={
                        <Mybutton
                            text={"왼쪽버튼"}
                            onClick={() => alert("왼쪽클릭")}
                        />
                    }
                    rightChild={
                        <Mybutton
                            text={"오른쪽버튼"}
                            onClick={() => alert("오른쪽클릭")}
                        />
                    }
                />
                <h2>app.js</h2>
                <Mybutton
                    text={"버튼"}
                    onClick={() => alert("버튼클릭")}
                    type={"positive"}
                />
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/new" element={<New />} />
                    <Route path="/edit" element={<Edit />} />
                    <Route path="/diary/:id" element={<Diary />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;
