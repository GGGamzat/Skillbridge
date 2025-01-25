import Header from '../components/Header';
import Footer from '../components/Footer';
import play from '../assets/icons/play.svg';
import device_1 from '../assets/icons/device_1.svg';
import device_2 from '../assets/icons/device_2.svg';
import device_3 from '../assets/icons/device_3.svg';
import device_4 from '../assets/icons/device_4.svg';
import device_5 from '../assets/icons/device_5.svg';
import device_6 from '../assets/icons/device_6.svg';

function Home() {
    return (
        <>
            <Header />
            <main className="main">
                <div className="main__screen">
                    <div className="main-screen__body">
                        <h1 className="main-body__title">The Best Streaming Experience</h1>
                        <p className="main-body__text">StreamVibe is the best streaming experience for watching your favorite movies and shows on demand, anytime, anywhere. With StreamVibe, you can enjoy a wide variety of content, including the latest blockbusters, classic movies, popular TV shows, and more. You can also create your own watchlists, so you can easily find the content you want to watch.</p>
                        <button type="button" className="main-body__btn">
                            <img src={play} alt="" />
                            <span>Start Watching Now</span>
                        </button>
                    </div>
                </div>
                <section className="section__devices">
                    <h3 className="section-devices__title">We Provide you streaming experience across various devices.</h3>
                    <p className="section-devices__text">With StreamVibe, you can enjoy your favorite movies and TV shows anytime, anywhere. Our platform is designed to be compatible with a wide range of devices, ensuring that you never miss a moment of entertainment.</p>
                    <div className="devices">
                        <div className="block__device">
                            <div className="block-device__head">
                                <div className="device-head__icon"><img src={device_1} /></div>
                                <h5 className="device-head__title">Smartphones</h5>
                            </div>
                            <p className="block-device__text">StreamVibe is optimized for both Android and iOS smartphones. Download our app from the Google Play Store or the Apple App Store</p>
                        </div>
                        <div className="block__device">
                            <div className="block-device__head">
                                <div className="device-head__icon"><img src={device_2} /></div>
                                <h5 className="device-head__title">Tablet</h5>
                            </div>
                            <p className="block-device__text">StreamVibe is optimized for both Android and iOS smartphones. Download our app from the Google Play Store or the Apple App Store</p>
                        </div>
                        <div className="block__device">
                            <div className="block-device__head">
                                <div className="device-head__icon"><img src={device_3} /></div>
                                <h5 className="device-head__title">Smart TV</h5>
                            </div>
                            <p className="block-device__text">StreamVibe is optimized for both Android and iOS smartphones. Download our app from the Google Play Store or the Apple App Store</p>
                        </div>
                        <div className="block__device">
                            <div className="block-device__head">
                                <div className="device-head__icon"><img src={device_4} /></div>
                                <h5 className="device-head__title">Laptops</h5>
                            </div>
                            <p className="block-device__text">StreamVibe is optimized for both Android and iOS smartphones. Download our app from the Google Play Store or the Apple App Store</p>
                        </div>
                        <div className="block__device">
                            <div className="block-device__head">
                                <div className="device-head__icon"><img src={device_5} /></div>
                                <h5 className="device-head__title">Gaming Consoles</h5>
                            </div>
                            <p className="block-device__text">StreamVibe is optimized for both Android and iOS smartphones. Download our app from the Google Play Store or the Apple App Store</p>
                        </div>
                        <div className="block__device">
                            <div className="block-device__head">
                                <div className="device-head__icon"><img src={device_6} /></div>
                                <h5 className="device-head__title">VR Headsets</h5>
                            </div>
                            <p className="block-device__text">StreamVibe is optimized for both Android and iOS smartphones. Download our app from the Google Play Store or the Apple App Store</p>
                        </div>
                    </div>
                </section>
            </main>
            <Footer />
        </>
    );
}

export default Home;