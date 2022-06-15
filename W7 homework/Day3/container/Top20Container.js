import React, {useState, useEffect} from 'react';
import Top20List from '../components/Top20List';


const Top20Container = () => {
    const [songs, setSongs] = useState ([]);


    useEffect(() => {
      getSongs();
    }, [])

    const getSongs = function(){
        fetch('https://itunes.apple.com/gb/rss/topsongs/limit=20/json')
        .then(res => res.json())
        .then(data => setSongs(data.feed.entry))
    }
    return (

        <>
        <div>
            <Top20List songs={songs}/>

        </div>
        
        </>

    )
}

export default Top20Container