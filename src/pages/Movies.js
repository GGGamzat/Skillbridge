import React, { Component } from 'react';
import Header from '../components/Header';
import Slider from '../components/Slider';
import Movie_card from './Movie_card';

export class Movies extends Component {
    render() {
        return (
            <>
                <Header />
                <main class="main">
                    <div class="main__container">
                        <Slider />
                        <div class="movie-list">
                            <div class="movie-list__container">
                                <div class="movie-card">
                                    {this.props.movies.map((movie) => (
                                        <Movie_card key={movie.id} movie={movie} />
                                    ))}
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
            </>
        );
    }
}

export default Movies;