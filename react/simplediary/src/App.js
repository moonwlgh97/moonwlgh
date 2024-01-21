import './App.css';
import DiaryEditor from './DiaryEditor';
import DiaryList from './DiaryList';


const dummyList = [
  {
    id:1,
    author :"문지호",
    content:"하이",
    emotion:5,
    create_date: new Date().getTime()
  },
  {
    id:2,
    author :"문지호1",
    content:"하이2",
    emotion:3,
    create_date: new Date().getTime()
  },
  {
    id:3,
    author :"문지호2",
    content:"하이3",
    emotion:4,
    create_date: new Date().getTime()
  },
 
]


function App() {
  return (
    <div className="App">
     
     <DiaryEditor/>
     <DiaryList diaryList={dummyList}/>
    </div>
  );
}

export default App;
