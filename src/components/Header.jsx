import logo from '../assets/icons/logo.svg';
import search from '../assets/icons/search.svg';
import bell from '../assets/icons/bell.svg';
import { useNavigate } from 'react-router-dom';

function Header() {
    const navigate = useNavigate();
    return(
        <header className="header">
            <div className="header__container">
                <a href="#"><img src={logo} class="header__logo" alt="" /></a>
                <nav className="menu">
                    <div className="menu__container">
                        <button className="menu__btn" onClick={() => navigate('/')}>Home</button>
                        <button className="menu__btn" onClick={() => navigate('movies')}>Movies & Shows</button>
                        <button className="menu__btn">Support</button>
                        <button className="menu__btn">Subscriptions</button>
                    </div>
                </nav>
                <div className="header__actions">
                    <a href="#"><img src={search} className="header-action__search" alt="" /></a>
                    <a href="#"><img src={bell} className="header-action__bell" alt="" /></a>
                </div>
            </div>
        </header>
    );
}

export default Header;