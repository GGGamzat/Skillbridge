import React, { Component } from 'react';

export class Movie extends Component {
    render() {
        return (
            <>
                <div class="movie-card__title">{this.props.movie.title}</div>
                <img src={"./img/" + this.props.movie.img}></img>
            </>
        );
    }
}

export default Movie;