/**
 * Returns a promise with from the Courses API
 * @returns Promise
 */
export default async () => {
  const res = await fetch('https://us-east1-memento-mori-universitas.cloudfunctions.net/gcp-read-courses-cf');
  return res.json();
};