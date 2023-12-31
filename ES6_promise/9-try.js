export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (e) {
    const { name, message } = e;
    queue.push(`${name}: ${message}`);
  }
  queue.push('Guardrail was processed');
  return queue;
}
