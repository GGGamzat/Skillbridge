import play from '../assets/icons/play.svg';

function Main() {
    return(
        <main className="main">
            <div class="main__screen">
                <div className="main-screen__body">
                    <h1 className="main-body__title">The Best Streaming Experience</h1>
                    <p className="main-body__text">StreamVibe is the best streaming experience for watching your favorite movies and shows on demand, anytime, anywhere. With StreamVibe, you can enjoy a wide variety of content, including the latest blockbusters, classic movies, popular TV shows, and more. You can also create your own watchlists, so you can easily find the content you want to watch.</p>
                    <button type="button" className="main-body__btn">
                        <img src={play} alt="" />
                        <span>Start Watching Now</span>
                    </button>
                </div>
            </div>
        </main>
    );
}

export default Main;