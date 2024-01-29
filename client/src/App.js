import { ChakraProvider } from "@chakra-ui/react";
import "./App.css";
import Landing from "./Landing";
import CreateGroup from "./CreateGroup"; // 컴포넌트 이름 대문자로 시작
import { BrowserRouter, Route, Routes } from "react-router-dom";

function App() {
    return (
        <div className="App">
            <ChakraProvider>
                <BrowserRouter>
                    <Routes>
                        <Route path="/" element={<Landing />} />
                        <Route path="/createGroup" element={<CreateGroup />} />
                    </Routes>
                </BrowserRouter>
            </ChakraProvider>
        </div>
    );
}

export default App;
