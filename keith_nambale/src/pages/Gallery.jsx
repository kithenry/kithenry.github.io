export default function Gallery() {
  return (
    <section>
      <h2 className="text-3xl font-serif mb-4">Gallery</h2>
      <p>Sunrise photos, tech snapshots, and more.</p>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mt-4">
        <div className="bg-gray-300 h-40">📷 Photo 1</div>
        <div className="bg-gray-300 h-40">📷 Photo 2</div>
        <div className="bg-gray-300 h-40">📷 Photo 3</div>
      </div>
    </section>
  );
}
