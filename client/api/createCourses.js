/**
 * Returns a promise with from the Courses API to create a course
 * @returns Promise
 */
export default async (payload) => {
  const res = await fetch('https://us-east1-memento-mori-universitas.cloudfunctions.net/gcp-write-courses-cf', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ name: payload.name, description: payload.description })
  });
  return res.json();
};