import React from 'react';

const Song = ({song, index}) => {
  


    return (
        <li>
            <h4>{index + 1}</h4>
            <p>Title: {song["im:name"].label}</p>
            <p>By: {song["im:artist"].label}</p>
        </li>
    )
}

export default Song;