import React from 'react';

const Film = ({film}) => {

    return (
        <h4><a href={film.url}>{film.name}</a></h4>
    )
}

export default Film