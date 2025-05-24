import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-[#8B5E3C] text-white py-4 px-6 flex justify-between items-center">
      <h1 className="text-2xl font-serif">K(e)ith N. Henry</h1>
      <div className="space-x-4 text-sm">
        <Link to="/">Home</Link>
        <Link to="/projects">Projects</Link>
        <Link to="/gallery">Gallery</Link>
        <Link to="/about">About</Link>
      </div>
    </nav>
  );
}
