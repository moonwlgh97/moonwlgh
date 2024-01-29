import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Edit from "./pages/Edit";
import New from "./pages/New";
import Diary from "./pages/Diary";

// components
import Mybutton from "./components/Mybutton";
import MyHeader from "./components/MyHeader";
import { useReducer, useRef } from "react";

const reducer = (state, action) => {
    let newState = [];

    switch (action.type) {
        case "INIT": {
            return action.data;
        }
        case "CREATE": {
            const newItem = {
                ...action.data,
            };
            newState = [newItem, ...state];
            break;
        }
        case "REMOVE": {
            newState = state.filter((it) => it.id !== action.target.id);
            break;
        }
        case "EDIT": {
            newState = state.map((it) =>
                it.id === action.data.id ? { ...action.data } : it,
            );
            break;
        }
        default:
            return state;
    }
    return newState;
};

function App() {
    const [data, dispatch] = useReducer(reducer, []);

    const dataId = useRef(0);

    //create

    const onCreate = (date, content, emotion) => {
        dispatch({
            type: "CREATE",
            data: {
                id: dataId.current,
                data: new Date(date).getTime(),
                content,
                emotion,
            },
        });
        dataId.current += 1;
    };

    //move

    const onRemove = (targetId) => {
        dispatch({ type: "REMOVE", targetId });
    };

    //EDIT
    const onEdit = (targetId, date, content, emotion) => {
        dispatch({
            type: "EDIT",
            data: {
                id: targetId,
                date: new Date(date).getTime(),
                content,
                emotion,
            },
        });
    };

    return (
        <BrowserRouter>
            <div className="App">
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
