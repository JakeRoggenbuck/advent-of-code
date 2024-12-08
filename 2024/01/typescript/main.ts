function part_one(text: string): Number {
  const lines = text.split('\n');

  let total = 0;

  let left = [];
  let right = [];

  for (let i = 0; i < lines.length; i++) {
    const [a, b] = lines[i].split('  ');

    if (lines[i] !== '') {
      left.push(Number(a));
      right.push(Number(b));
    }
  }

  left.sort();
  right.sort();

  for (let i = 0; i < left.length; i++) {
    let c = left[i] - right[i];
    total += Math.abs(c);
  }

  return total;
}

function part_two(text: string): Number {
  const lines = text.split('\n');

  let total = 0;

  let left = [];
  let right = [];

  for (let i = 0; i < lines.length; i++) {
    const [a, b] = lines[i].split('  ');

    if (lines[i] !== '') {
      left.push(Number(a));
      right.push(Number(b));
    }
  }

  for (let i = 0; i < left.length; i++) {
    total += right.filter((x) => x === left[i]).length * left[i];
  }

  return total;
}

if (import.meta.main) {
  const text: string = await Deno.readTextFile('../input');

  const p1 = part_one(text);
  console.log(p1);

  const p2 = part_two(text);
  console.log(p2);
}
