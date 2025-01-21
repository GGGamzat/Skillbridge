import slide_1 from '../public/slides/1.jpg';
import slide_2 from '../public/slides/2.jpeg';
import slide_3 from '../public/slides/3.jpg';
import slide_4 from '../public/slides/4.jpg';
import slide_5 from '../public/slides/5.jpg';
import arrow_left from '../assets/icons/arrow_left.svg';
import arrow_right from '../assets/icons/arrow_right.svg';
import play from '../assets/icons/play.svg';
import plus from '../assets/icons/plus.svg';

function Slider() {
    return(
        <div class="slider">
            <div class="list">
                <div class="item">
                    <img class="slide-img" src={slide_1} alt="" />
                    <div class="slide__info">
                        <h1>Джокер</h1>
                        <p>Готэм, начало 1980-х годов. Комик Артур Флек живет с больной матерью, которая с детства учит его «ходить с улыбкой». Пытаясь нести в мир хорошее и дарить людям радость, Артур сталкивается с человеческой жестокостью и постепенно приходит к выводу, что этот мир получит от него не добрую улыбку, а ухмылку злодея Джокера.</p>
                        <div class="slide-info__btns">
                            <button class="btn-play">
                                <img src={play} alt="" />
                                Play Now
                            </button>
                            <button class="slide-info__btn"><img src={plus} alt="" /></button>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <img class="slide-img" src={slide_2} alt="" />
                    <div class="slide__info">
                        <h1>Темный рыцарь</h1>
                        <p>Бэтмен поднимает ставки в войне с криминалом. С помощью лейтенанта Джима Гордона и прокурора Харви Дента он намерен очистить улицы Готэма от преступности.</p>
                        <div class="slide-info__btns">
                            <button class="btn-play">
                                <img src={play} alt="" />
                                Play Now
                            </button>
                            <button class="slide-info__btn"><img src={plus} alt="" /></button>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <img class="slide-img" src={slide_3} alt="" />
                    <div class="slide__info">
                        <h1>Омерзительная восьмерка</h1>
                        <p>США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пёстрое общество: генерал конфедератов, мексиканец, ковбой… И один из них — не тот, за кого себя выдает.</p>
                        <div class="slide-info__btns">
                            <button class="btn-play">
                                <img src={play} alt="" />
                                Play Now
                            </button>
                            <button class="slide-info__btn"><img src={plus} alt="" /></button>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <img class="slide-img" src={slide_4} alt="" />
                    <div class="slide__info">
                        <h1>Крестный отец 2</h1>
                        <p>Для дона Корлеоне и его сына не существует моральных преград на пути к достижению целей. Они превращают мафию, построенную по патриархальным сицилийским законам, в весьма прагматичную, жесткую корпорацию, плавно интегрируя её в большой бизнес Америки.</p>
                        <div class="slide-info__btns">
                            <button class="btn-play">
                                <img src={play} alt="" />
                                Play Now
                            </button>
                            <button class="slide-info__btn"><img src={plus} alt="" /></button>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <img class="slide-img" src={slide_5} alt="" />
                    <div class="slide__info">
                        <h1>Отступники</h1>
                        <p>Два лучших выпускника полицейской академии оказались по разные стороны баррикады: один из них — агент мафии в рядах правоохранительных органов, другой — «крот», внедрённый в мафию. Каждый считает своим долгом обнаружить и уничтожить противника.</p>
                        <div class="slide-info__btns">
                            <button class="btn-play">
                                <img src={play} alt="" />
                                Play Now
                            </button>
                            <button class="slide-info__btn"><img src={plus} alt="" /></button>
                        </div>
                    </div>
                </div>
            </div>
            <div class='test'>
                <button id="prev"><img src={arrow_left} alt="" /></button>
                <ul class="dots">
                    <li class="active"></li>
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