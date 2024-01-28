import { ChakraProvider } from "@chakra-ui/react";
import "./App.css";
import Landing from "./Landing";

function App() {
    return (
    <div className="App">
        <ChakraProvider>
            <Landing/>
        </ChakraProvider>
    </div>
    );
}

export default App;
