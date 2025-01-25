import slide_1 from '../assets/images/1.jpg';
import slide_2 from '../assets/images/2.jpeg';
import slide_3 from '../assets/images/3.jpg';
import slide_4 from '../assets/images/4.jpg';
import slide_5 from '../assets/images/5.jpg';
import arrow_left from '../assets/icons/arrow_left.svg';
import arrow_right from '../assets/icons/arrow_right.svg';
import play from '../assets/icons/play.svg';
import plus from '../assets/icons/plus.svg';

function Slider() {
    return(
        <div className="slider">
            <div className="list">
                <div className="item">
                    <img className="slide-img" src={slide_1} alt="" />
                    <div className="slide__info">
                        <h1>title1</h1>
                        <p>text1</p>
                        <div className="slide-info__btns">
                            <button className="btn-play">
                                <img src={play} alt="" />
                                Play Now
                            </button>
                            <button className="slide-info__btn"><img src={plus} alt="" /></button>
                        </div>
                    </div>
                </div>
                <div className="item">
                    <img className="slide-img" src={slide_2} alt="" />
                    <div className="slide__info">
                        <h1>title2</h1>
                        <p>text2</p>
                        <div className="slide-info__btns">
                            <button className="btn-play">
                                <img src={play} alt="" />
                                Play Now
                            </button>
                            <button className="slide-info__btn"><img src={plus} alt="" /></button>
                        </div>
                    </div>
                </div>
                <div className="item">
                    <img className="slide-img" src={slide_3} alt="" />
                    <div className="slide__info">
                        <h1>title3</h1>
                        <p>text3</p>
                        <div className="slide-info__btns">
                            <button className="btn-play">
                                <img src={play} alt="" />
                                Play Now
                            </button>
                            <button className="slide-info__btn"><img src={plus} alt="" /></button>
                        </div>
                    </div>
                </div>
                <div className="item">
                    <img className="slide-img" src={slide_4} alt="" />
                    <div className="slide__info">
                        <h1>title4</h1>
                        <p>text4</p>
                        <div className="slide-info__btns">
                            <button className="btn-play">
                                <img src={play} alt="" />
                                Play Now
                            </button>
                            <button className="slide-info__btn"><img src={plus} alt="" /></button>
                        </div>
                    </div>
                </div>
                <div className="item">
                    <img className="slide-img" src={slide_5} alt="" />
                    <div className="slide__info">
                        <h1>title5</h1>
                        <p>text5</p>
                        <div className="slide-info__btns">
                            <button className="btn-play">
                                <img src={play} alt="" />
                                Play Now
                            </button>
                            <button className="slide-info__btn"><img src={plus} alt="" /></button>
                        </div>
                    </div>
                </div>
            </div>
            <div className='nav-slider'>
                <button id="prev"><img src={arrow_left} alt="" /></button>
                <ul className="dots">
                    <li className="active"></li>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
                <button id="next"><img src={arrow_right} alt="" /></button>
            </div>
        </div>
    );
}

export default Slider;