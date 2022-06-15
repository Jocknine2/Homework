import React from 'react';
import Song from './Song';

const Top20List = ({songs}) => {

    const songsItems = songs.map((song, index) => {
        return <Song song={song} key={index} index={index}/>
    })

    return (
        <div>
            <ul>
                {songsItems}
            </ul>
        </div>

    )
}

export default Top20List