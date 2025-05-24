import React from "react";

export default function HomePage() {
  return (
    <div className="min-h-screen bg-[#f4f1ea] text-[#382110] font-serif">
      {/* Navbar */}
      <nav className="bg-[#382110] text-white p-4 flex justify-between items-center sticky top-0 z-10">
        <h1 className="text-2xl font-bold">Books & Bytes</h1>
        <ul className="flex gap-6 text-sm font-light">
          <li className="hover:underline cursor-pointer">Projects</li>
          <li className="hover:underline cursor-pointer">Gallery</li>
          <li className="hover:underline cursor-pointer">About</li>
          <li className="hover:underline cursor-pointer">Contact</li>
        </ul>
      </nav>

      {/* Hero Section */}
      <section className="p-10 text-center">
        <h2 className="text-5xl mb-4">Hi there! 👋</h2>
        <p className="max-w-2xl mx-auto text-lg mb-6">
          I’m a Computer Engineering student exploring Web Dev, AI, and Robotics. I also log my journey here.
        </p>
        <p className="mb-8">Have a look around and join me on this ride!</p>
        <div className="flex justify-center gap-4">
          <button className="border-2 border-[#6c8e5e] text-[#6c8e5e] px-6 py-2 rounded-md hover:bg-[#6c8e5e] hover:text-white transition">
            📚 Explore Projects
          </button>
          <button className="border-2 border-[#6c8e5e] text-[#6c8e5e] px-6 py-2 rounded-md hover:bg-[#6c8e5e] hover:text-white transition">
            🧑‍💻 About Me
          </button>
        </div>
      </section>

      {/* About Section */}
      <section className="flex flex-col md:flex-row items-center justify-center gap-12 px-8 py-16 bg-[#eae7dc]">
        <img
          src="https://via.placeholder.com/200"
          alt="Profile"
          className="rounded-full w-48 h-48 object-cover"
        />
        <div className="text-center md:text-left max-w-md">
          <h3 className="text-3xl mb-2">ABOUT ME</h3>
          <p className="mb-4">Software | Hardware | Python | C++ | Django | React | AI</p>
          <button className="border-2 border-[#6c8e5e] text-[#6c8e5e] px-5 py-2 rounded hover:bg-[#6c8e5e] hover:text-white transition">
            📬 Contact Me
          </button>
        </div>
      </section>

      {/* Social Icons */}
      <section className="py-12 text-center">
        <h4 className="text-xl mb-6">FOLLOW</h4>
        <div className="flex justify-center gap-6 text-2xl">
          <a href="#" className="hover:text-[#6c8e5e]">🐙</a>
          <a href="#" className="hover:text-[#6c8e5e]">✈️</a>
          <a href="#" className="hover:text-[#6c8e5e]">🐦</a>
          <a href="#" className="hover:text-[#6c8e5e]">💼</a>
          <a href="#" className="hover:text-[#6c8e5e]">🎮</a>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-[#d9cec3] text-center py-4 text-sm text-[#382110]">
        © 2025 Books & Bytes. All Rights Reserved.
      </footer>
    </div>
  );
}
