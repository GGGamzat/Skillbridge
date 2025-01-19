import facebook from '../assets/icons/facebook.svg';
import twitter from '../assets/icons/twitter.svg';
import linkedin from '../assets/icons/linkedin.svg';

function Footer() {
    return(
        <footer className="footer">
            <div className="footer__container">
                <div className="block__main">
                    <nav className="footer__nav">
                        <a href="" className="footer-nav__title">Home</a>
                        <ul>
                            <li><a href="">Categories</a></li>
                            <li><a href="">Devices</a></li>
                            <li><a href="">Pricing</a></li>
                            <li><a href="">FAQ</a></li>
                        </ul>
                    </nav>
                    <nav className="footer__nav">
                        <a href="" className="footer-nav__title">Movies</a>
                        <ul>
                            <li><a href="">Gerner</a></li>
                            <li><a href="">Trending</a></li>
                            <li><a href="">New Release</a></li>
                            <li><a href="">Popular</a></li>
                        </ul>
                    </nav>
                    <nav className="footer__nav">
                        <a href="" className="footer-nav__title">Shows</a>
                        <ul>
                            <li><a href="">Gerner</a></li>
                            <li><a href="">Trending</a></li>
                            <li><a href="">New Release</a></li>
                            <li><a href="">Popular</a></li>
                        </ul>
                    </nav>
                    <nav className="footer__nav">
                        <a href="" className="footer-nav__title">Support</a>
                        <ul>
                            <li><a href="">Contact Us</a></li>
                        </ul>
                    </nav>
                    <nav className="footer__nav">
                        <a href="" className="footer-nav__title">Subscription</a>
                        <ul>
                            <li><a href="">Plans</a></li>
                            <li><a href="">Features</a></li>
                        </ul>
                    </nav>
                    <nav className="footer__nav">
                        <a href="" className="footer-nav__title">Connect With Us</a>
                        <div className="footer__btns">
                            <button className="footer__btn">
                                <img src={facebook} alt="" />
                            </button>
                            <button className="footer__btn">
                                <img src={twitter} alt="" />
                            </button>
                            <button className="footer__btn">
                                <img src={linkedin} alt="" />
                            </button>
                        </div>
                    </nav>
                </div>
                <div className="block__info">
                    <span>@2023 streamvib, All Rights Reserved</span>
                    <nav className="block-info__nav">
                        <ul>
                            <li><a href="">Terms of Use</a></li>
                            <li>|</li>
                            <li><a href="">Privacy Policy</a></li>
                            <li>|</li>
                            <li><a href="">Cookie Policy</a></li>
                        </ul>
                    </nav>
                </div>
            </div>
        </footer>
    );
}

export default Footer;