# [Airbnb JavaScript Style Guide][1]

## References

- 2.1: Use `const` for all of your references; avoid using `var`.
- 2.2: If you must reassign references, use `let` instead of `var`.
- 2.3: Note that both `let` and `const` are block-scoped, whereas `var` is function-scoped.

## Objects

- 3.2: Use computed property names when creating objects with dynamic property names.
  - Why? They allow you to define all the properties of an object in one place.

```javascript
function getKey(k) {
  return `a key named ${k}`;
}

// bad
const obj = {
  id: 5,
  name: 'San Francisco',
};
obj[getKey('enabled')] = true;

// good
const obj = {
  id: 5,
  name: 'San Francisco',
  [getKey('enabled')]: true,
};
```

- 3.3: Use object method shorthand.

```javascript
// bad
const atom = {
  value: 1,

  addValue: function (value) {
    return atom.value + value;
  },
};

// good
const atom = {
  value: 1,

  addValue(value) {
    return atom.value + value;
  },
};
```

- 3.4: Use property value shorthand.
  - Why? It is shorter and descriptive.

```javascript
const lukeSkywalker = 'Luke Skywalker';

// bad
const obj = {
  lukeSkywalker: lukeSkywalker,
};

// good
const obj = {
  lukeSkywalker,
};
```

- 3.5: Group your shorthand properties at the beginning of your object declaration.
  - Why? It’s easier to tell which properties are using the shorthand.

- 3.6: Only quote properties that are invalid identifiers.
  - In general we consider it subjectively easier to read.
    It improves syntax highlighting, and is also more easily optimized by many JS engines.

```javascript
// bad
const bad = {
  'foo': 3,
  'bar': 4,
  'data-blah': 5,
};

// good
const good = {
  foo: 3,
  bar: 4,
  'data-blah': 5,
};
```

- 3.8: Prefer the object spread syntax over `Object.assign` to shallow-copy objects.
  Use the object rest parameter syntax to get a new object with certain properties omitted. 

```javascript
// very bad
const original = { a: 1, b: 2 };
const copy = Object.assign(original, { c: 3 }); // this mutates `original` ಠ_ಠ
delete copy.a; // so does this

// bad
const original = { a: 1, b: 2 };
const copy = Object.assign({}, original, { c: 3 }); // copy => { a: 1, b: 2, c: 3 }

// good
const original = { a: 1, b: 2 };
const copy = { ...original, c: 3 }; // copy => { a: 1, b: 2, c: 3 }

const { a, ...noA } = copy; // noA => { b: 2, c: 3 }
```

## Arrays

- 4.2: Use `Array#push` instead of direct assignment to add items to an array.

- 4.3: Use array spreads `...` to copy arrays.

```javascript
// bad
const len = items.length;
const itemsCopy = [];
let i;

for (i = 0; i < len; i += 1) {
  itemsCopy[i] = items[i];
}

// good
const itemsCopy = [...items];
```

- 4.4: To convert an iterable object to an array, use spreads `...` instead of `Array.from`.

```javascript
const foo = document.querySelectorAll('.foo');

// good
const nodes = Array.from(foo);

// best
const nodes = [...foo];
```

- 4.5: Use return statements in array method callbacks.
  It’s ok to omit the return if the function body consists of a single statement returning an expression without side effects.

```javascript
// good
[1, 2, 3].map((x) => {
  const y = x + 1;
  return x * y;
});

// good
[1, 2, 3].map((x) => x + 1);

// bad - no returned value means `acc` becomes undefined after the first iteration
[[0, 1], [2, 3], [4, 5]].reduce((acc, item, index) => {
  const flatten = acc.concat(item);
});

// good
[[0, 1], [2, 3], [4, 5]].reduce((acc, item, index) => {
  const flatten = acc.concat(item);
  return flatten;
});
```

## Destructuring

- 5.1: Use object destructuring when accessing and using multiple properties of an object.
  - Why? Destructuring saves you from creating temporary references for those properties,
    and from repetitive access of the object. It is also more readable.

```javascript
// bad
function getFullName(user) {
  const firstName = user.firstName;
  const lastName = user.lastName;

  return `${firstName} ${lastName}`;
}

// good
function getFullName(user) {
  const { firstName, lastName } = user;
  return `${firstName} ${lastName}`;
}

// best
function getFullName({ firstName, lastName }) {
  return `${firstName} ${lastName}`;
}
```

- 5.2: Use array destructuring. 

```javascript
const arr = [1, 2, 3, 4];

// bad
const first = arr[0];
const second = arr[1];

// good
const [first, second] = arr;
```

- 5.3: Use object destructuring for multiple return values, not array destructuring.
  - Why? You can add new properties over time or change the order of things without breaking call sites.

```javascript
// bad
function processInput(input) {
  // then a miracle occurs
  return [left, right, top, bottom];
}

// the caller needs to think about the order of return data
const [left, __, top] = processInput(input);

// good
function processInput(input) {
  // then a miracle occurs
  return { left, right, top, bottom };
}

// the caller selects only the data they need
const { left, top } = processInput(input);
```

## String

- 6.3: When programmatically building up strings, use template strings instead of concatenation.

```javascript
// bad
function sayHi(name) {
  return 'How are you, ' + name + '?';
}

// bad
function sayHi(name) {
  return ['How are you, ', name, '?'].join();
}

// bad
function sayHi(name) {
  return `How are you, ${ name }?`;
}

// good
function sayHi(name) {
  return `How are you, ${name}?`;
}
```

- 6.4: Never use `eval()` on a string, it opens too many vulnerabilities.

- 6.5: Do not unnecessarily escape characters in strings.
  - Why? Backslashes harm readability, thus they should only be present when necessary.

```javascript
// bad
const foo = '\'this\' \i\s \"quoted\"';

// good
const foo = '\'this\' is "quoted"';
const foo = `my name is '${name}'`;
```

## Functions

- 7.4: Never declare a function in a non-function block (if, while, etc). Assign the function to a variable instead.
  - Writing functions within loops tends to result in errors due to the way the function creates a closure around the loop.

- 7.5: Never name a parameter arguments.
  - This will take precedence over the arguments object that is given to every function scope.

- 7.6: Never use arguments, opt to use rest syntax `...` instead.
  - `...` is explicit about which arguments you want pulled.
  - Plus, rest arguments are a real Array, and not merely Array-like like `arguments`.

```javascript
// bad
function concatenateAll() {
  const args = Array.prototype.slice.call(arguments);
  return args.join('');
}

// good
function concatenateAll(...args) {
  return args.join('');
}
```

- 7.7: Use default parameter syntax rather than mutating function arguments.

```javascript
// really bad
function handleThings(opts) {
  // No! We shouldn’t mutate function arguments.
  // Double bad: if opts is falsy it'll be set to an object which may
  // be what you want but it can introduce subtle bugs.
  opts = opts || {};
  // ...
}

// still bad
function handleThings(opts) {
  if (opts === void 0) {
    opts = {};
  }
  // ...
}

// good
function handleThings(opts = {}) {
  // ...
}
```

- 7.12: Never mutate parameters.
  - Why? Manipulating objects passed in as parameters can cause unwanted variable side effects in the original caller.

```javascript
// bad
function f1(obj) {
  obj.key = 1;
}

// good
function f2(obj) {
  const key = Object.prototype.hasOwnProperty.call(obj, 'key') ? obj.key : 1;
}
```

## Arrow Functions

- 8.1: When you must use an anonymous function (as when passing an inline callback), use arrow function notation.
  - Why? It creates a version of the function that executes in the context of this, which is usually what you want, and is a more concise syntax.
  - Why not? If you have a fairly complicated function, you might move that logic out into its own named function expression.

```javascript
// bad
[1, 2, 3].map(function (x) {
  const y = x + 1;
  return x * y;
});

// good
[1, 2, 3].map((x) => {
  const y = x + 1;
  return x * y;
});
```

- 8.2: If the function body consists of a single statement returning an expression without side effects, omit the braces and use the implicit return.
  Otherwise, keep the braces and use a return statement.
  - Why? Syntactic sugar. It reads well when multiple functions are chained together.

```javascript
// bad
[1, 2, 3].map((number) => {
  const nextNumber = number + 1;
  `A string containing the ${nextNumber}.`;
});

// good
[1, 2, 3].map((number) => `A string containing the ${number + 1}.`);

// good
[1, 2, 3].map((number) => {
  const nextNumber = number + 1;
  return `A string containing the ${nextNumber}.`;
});

// good
[1, 2, 3].map((number, index) => ({
  [index]: number,
}));

// No implicit return with side effects
function foo(callback) {
  const val = callback();
  if (val === true) {
    // Do something if callback returns true
  }
}

let bool = false;

// bad
foo(() => bool = true);

// good
foo(() => {
  bool = true;
});
```

- 8.4: Always include parentheses around arguments for clarity and consistency.
  - Why? Minimizes diff churn when adding or removing arguments.

```javascript
// bad
[1, 2, 3].map(x => x * x);

// good
[1, 2, 3].map((x) => x * x);
```

- 8.5: Avoid confusing arrow function syntax (=>) with comparison operators (<=, >=).

```javascript
// bad
const itemHeight = (item) => item.height <= 256 ? item.largeSize : item.smallSize;

// bad
const itemHeight = (item) => item.height >= 256 ? item.largeSize : item.smallSize;

// good
const itemHeight = (item) => (item.height <= 256 ? item.largeSize : item.smallSize);

// good
const itemHeight = (item) => {
  const { height, largeSize, smallSize } = item;
  return height <= 256 ? largeSize : smallSize;
};
```

## Classes & Constructors

- 9.3: Methods can return this to help with method chaining.

```javascript
// bad
Jedi.prototype.jump = function () {
  this.jumping = true;
  return true;
};

Jedi.prototype.setHeight = function (height) {
  this.height = height;
};

const luke = new Jedi();
luke.jump(); // => true
luke.setHeight(20); // => undefined

// good
class Jedi {
  jump() {
    this.jumping = true;
    return this;
  }

  setHeight(height) {
    this.height = height;
    return this;
  }
}

const luke = new Jedi();

luke.jump()
  .setHeight(20);
```

- 9.4: It's okay to write a custom `toString()` method, just make sure it works successfully and causes no side effects.

```javascript
class Jedi {
  constructor(options = {}) {
    this.name = options.name || 'no name';
  }

  getName() {
    return this.name;
  }

  toString() {
    return `Jedi - ${this.getName()}`;
  }
}
```

- 9.5: Classes have a default constructor if one is not specified.
  An empty constructor function or one that just delegates to a parent class is unnecessary.

```javascript
// bad
class Jedi {
  constructor() {}

  getName() {
    return this.name;
  }
}

// bad
class Rey extends Jedi {
  constructor(...args) {
    super(...args);
  }
}

// good
class Rey extends Jedi {
  constructor(...args) {
    super(...args);
    this.name = 'Rey';
  }
}
```

- 9.7: Class methods should use `this` or be made into a static method unless an external library or framework requires using specific non-static methods.
  Being an instance method should indicate that it behaves differently based on properties of the receiver.

```javascript
// bad
class Foo {
  bar() {
    console.log('bar');
  }
}

// good - this is used
class Foo {
  bar() {
    console.log(this.bar);
  }
}

// good - constructor is exempt
class Foo {
  constructor() {
    // ...
  }
}

// good - static methods aren't expected to use this
class Foo {
  static bar() {
    console.log('bar');
  }
}
```

## Modules

- 10.1: Always use modules (import/export) over a non-standard module system. You can always transpile to your preferred module system.
  - Why? Modules are the future, let’s start using the future now.

```javascript
// bad
const AirbnbStyleGuide = require('./AirbnbStyleGuide');
module.exports = AirbnbStyleGuide.es6;

// ok
import AirbnbStyleGuide from './AirbnbStyleGuide';
export default AirbnbStyleGuide.es6;

// best
import { es6 } from './AirbnbStyleGuide';
export default es6;
```

- 10.2: Do not use wildcard imports.
  - Why? This makes sure you have a single default export.

```javascript
// bad
import * as AirbnbStyleGuide from './AirbnbStyleGuide';

// good
import AirbnbStyleGuide from './AirbnbStyleGuide';
```

- 10.3: And do not export directly from an import.
  - Why? Although the one-liner is concise, having one clear way to import and one clear way to export makes things consistent.

```javascript
// bad
// filename es6.js
export { es6 as default } from './AirbnbStyleGuide';

// good
// filename es6.js
import { es6 } from './AirbnbStyleGuide';
export default es6;
```

- 10.4: Only import from a path in one place.
  - Why? Having multiple lines that import from the same path can make code harder to maintain.

```javascript
// bad
import foo from 'foo';
// … some other imports … //
import { named1, named2 } from 'foo';

// good
import foo, { named1, named2 } from 'foo';

// good
import foo, {
  named1,
  named2,
} from 'foo';
```

- 10.5: Do not export mutable bindings.
  - Why? Mutation should be avoided in general, but in particular when exporting mutable bindings.
  - While this technique may be needed for some special cases, in general, only constant references should be exported.

```javascript
// bad
let foo = 3;
export { foo };

// good
const foo = 3;
export { foo };
```

- 10.6: In modules with a single export, prefer default export over named export.
  - Why? To encourage more files that only ever export one thing, which is better for readability and maintainability.

```javascript
// bad
export function foo() {}

// good
export default function foo() {}
```

- 10.7: Put all imports above non-import statements.
  - Why? Since imports are hoisted, keeping them all at the top prevents surprising behavior.

```javascript
// bad
import foo from 'foo';
foo.init();

import bar from 'bar';

// good
import foo from 'foo';
import bar from 'bar';

foo.init();
```

- 10.10: Do not include JavaScript filename extensions.
  - Why? Including extensions inhibits refactoring,
    and inappropriately hardcodes implementation details of the module you're importing in every consumer.

```javascript
// bad
import foo from './foo.js';
import bar from './bar.jsx';
import baz from './baz/index.jsx';

// good
import foo from './foo';
import bar from './bar';
import baz from './baz';
```

## Iterators and Generators

- 11.1: Don't use iterators. Prefer JavaScript's higher-order functions instead of loops like `for-in` or `for-of`.
  - Why? This enforces our immutable rule. Dealing with pure functions that return values is easier to reason about than side effects.
  - Use `map() / every() / filter() / find() / findIndex() / reduce() / some() / ...` to iterate over arrays,
    and `Object.keys() / Object.values() / Object.entries()` to produce arrays so you can iterate over objects.

```javascript
const numbers = [1, 2, 3, 4, 5];

// bad
let sum = 0;
for (let num of numbers) {
  sum += num;
}
sum === 15;

// good
let sum = 0;
numbers.forEach((num) => {
  sum += num;
});
sum === 15;

// best (use the functional force)
const sum = numbers.reduce((total, num) => total + num, 0);
sum === 15;

// bad
const increasedByOne = [];
for (let i = 0; i < numbers.length; i++) {
  increasedByOne.push(numbers[i] + 1);
}

// good
const increasedByOne = [];
numbers.forEach((num) => {
  increasedByOne.push(num + 1);
});

// best (keeping it functional)
const increasedByOne = numbers.map((num) => num + 1);
```

- 11.2: Don't use generators for now.
  - Why? They don't transpile well to ES5.

## Properties

- 12.1: Use dot notation when accessing properties.

```javascript
const luke = {
  jedi: true,
  age: 28,
};

// bad
const isJedi = luke['jedi'];

// good
const isJedi = luke.jedi;
```

- 12.2: Use bracket notation `[]` when accessing properties with a variable.

```javascript
const luke = {
  jedi: true,
  age: 28,
};

function getProp(prop) {
  return luke[prop];
}

const isJedi = getProp('jedi');
```

- 12.3: Use exponentiation operator `**` when calculating exponentiations. 

## Variables

- 13.1: Always use const or let to declare variables.
  - Not doing so will result in global variables. We want to avoid polluting the global namespace.

- 13.3: Group all your `const`s and then group all your `let`s.

- 13.4: Assign variables where you need them, but place them in a reasonable place.

```javascript
// bad - unnecessary function call
function checkName(hasName) {
  const name = getName();

  if (hasName === 'test') {
    return false;
  }

  if (name === 'test') {
    this.setName('');
    return false;
  }

  return name;
}

// good
function checkName(hasName) {
  if (hasName === 'test') {
    return false;
  }

  const name = getName();

  if (name === 'test') {
    this.setName('');
    return false;
  }

  return name;
}
```

- 13.5: Don't chain variable assignments.
  - Why? Chaining variable assignments creates implicit global variables.

```javascript
// bad
(function example() {
  // JavaScript interprets this as
  // let a = ( b = ( c = 1 ) );
  // The let keyword only applies to variable a; variables b and c become
  // global variables.
  let a = b = c = 1;
}());

console.log(a); // throws ReferenceError
console.log(b); // 1
console.log(c); // 1

// good
(function example() {
  let a = 1;
  let b = a;
  let c = a;
}());

console.log(a); // throws ReferenceError
console.log(b); // throws ReferenceError
console.log(c); // throws ReferenceError

// the same applies for `const`
```

- 13.6: Avoid using unary increments and decrements (`++`, `--`). 

- 13.7: Avoid linebreaks before or after = in an assignment.
  If your assignment violates max-len, surround the value in parens.

```javascript
// bad
const foo =
  superLongLongLongLongLongLongLongLongFunctionName();

// bad
const foo
  = 'superLongLongLongLongLongLongLongLongString';

// good
const foo = (
  superLongLongLongLongLongLongLongLongFunctionName()
);

// good
const foo = 'superLongLongLongLongLongLongLongLongString';
```

## Comparison Operators & Equality

- 15.1: Use `===` and `!==` over `==` and `!=`. 

- 15.2: Conditional statements such as the `if` statement evaluate their expression using coercion with the `ToBoolean` abstract method and always follow these simple rules:
  - Objects evaluate to true
  - Undefined evaluates to false
  - Null evaluates to false
  - Booleans evaluate to the value of the boolean
  - Numbers evaluate to false if +0, -0, or NaN, otherwise true
  - Strings evaluate to false if an empty string '', otherwise true

```javascript
if ([0] && []) {
  // true
  // an array (even an empty one) is an object, objects will evaluate to true
}
```

- 15.3: Use shortcuts for booleans, but explicit comparisons for strings and numbers.

```javascript
// bad
if (isValid === true) {
  // ...
}

// good
if (isValid) {
  // ...
}

// bad
if (name) {
  // ...
}

// good
if (name !== '') {
  // ...
}

// bad
if (collection.length) {
  // ...
}

// good
if (collection.length > 0) {
  // ...
}
```

- 15.5: Use braces to create blocks in case and default clauses that contain lexical declarations (e.g. `let`, `const`, `function`, and `class`).
  - Why? Lexical declarations are visible in the entire switch block but only get initialized when assigned, which only happens when its case is reached.
  - This causes problems when multiple case clauses attempt to define the same thing.

- 15.6: Ternaries should not be nested and generally be single line expressions.

- 15.7: Avoid unneeded ternary statements.

```javascript
// bad
const foo = a ? a : b;
const bar = c ? true : false;
const baz = c ? false : true;

// good
const foo = a || b;
const bar = !!c;
const baz = !c;
```

- 15.8: When mixing operators, enclose them in parentheses.
  - The only exception is the standard arithmetic operators: `+`, `-`, and `**` since their precedence is broadly understood.
  - We recommend enclosing `/` and `*` in parentheses because their precedence can be ambiguous when they are mixed.

## Blocks

- 16.1: If an `if` block always executes a `return` statement, the subsequent else block is unnecessary.
  A `return` in an `else` if block following an `if` block that contains a `return` can be separated into multiple if blocks.

## Control Statements

- 17.1: In case your control statement (if, while etc.) gets too long or exceeds the maximum line length, each (grouped) condition could be put into a new line.
  The logical operator should begin the line.
  - Why? Requiring operators at the beginning of the line keeps the operators aligned and follows a pattern similar to method chaining.
  - This also improves readability by making it easier to visually follow complex logic.

- 17.2: Don't use selection operators in place of control statements.

```javascript
// bad
!isRunning && startRunning();

// good
if (!isRunning) {
  startRunning();
}
```

## Comments

- 18.1: Use `/** ... */` for multiline comments.

- 18.2: Use `//` for single line comments.
  - Place single line comments on a newline above the subject of the comment.
  - Put an empty line before the comment unless it’s on the first line of a block.

- 18.4: Prefixing your comments with `FIXME` or `TODO` helps other developers quickly understand
  if you're pointing out a problem that needs to be revisited,
  or if you're suggesting a solution to the problem that needs to be implemented.
  - These are different than regular comments because they are actionable.
  - The actions are `FIXME: -- need to figure this out` or `TODO: -- need to implement`.

- 18.5: Use `// FIXME:` to annotate problems.

- 18.6: Use `// TODO:` to annotate solutions to problems.

## Whitespace

- 19.5: End files with a single newline character.
  - Benefits of trailing newlines include the ability to concatenate or append to files
    as well as output files to the terminal without interfering with shell prompts.

- 19.7: Leave a blank line after blocks and before the next statement.

## Commas

- 20.1: Leading commas: **Nope**.

- 20.2: Additional trailing comma: **Yup**.
  - Why? This leads to cleaner git diffs.
  - Also, transpilers like Babel will remove the additional trailing comma in the transpiled code which means you don’t have to worry about the trailing comma problem in legacy browsers.

## Semicolons

- 21.1: **Yup**.
  - Why? When JavaScript encounters a line break without a semicolon,
    it uses a set of rules called Automatic Semicolon Insertion to determine whether it should regard that line break as the end of a statement,
    and (as the name implies) place a semicolon into your code before the line break if it thinks so.
  - ASI contains a few eccentric behaviors, though, and your code will break if JavaScript misinterprets your line break.
  - These rules will become more complicated as new features become a part of JavaScript.
  - Explicitly terminating your statements and configuring your linter to catch missing semicolons will help prevent you from encountering issues.

## Type Casting & Coercion

- 22.2: Strings:

```javascript
// => this.reviewScore = 9;

// bad
const totalScore = new String(this.reviewScore); // typeof totalScore is "object" not "string"

// bad
const totalScore = this.reviewScore + ''; // invokes this.reviewScore.valueOf()

// bad
const totalScore = this.reviewScore.toString(); // isn't guaranteed to return a string. (Question: why?)

// good
const totalScore = String(this.reviewScore);
```

- 22.3: Numbers: Use Number for type casting and parseInt always with a radix for parsing strings.

```javascript
const inputValue = '4';

// bad
const val = new Number(inputValue);

// bad
const val = +inputValue;

// bad
const val = inputValue >> 0;

// bad
const val = parseInt(inputValue);

// good
const val = Number(inputValue);

// good
const val = parseInt(inputValue, 10);
```

- 22.5: Note: Be careful when using bitshift operations.
  - Numbers are represented as 64-bit values, but bitshift operations always return a 32-bit integer (source).
  - Bitshift can lead to unexpected behavior for integer values larger than 32 bits.

```javascript
2147483647 >> 0; // => 2147483647
2147483648 >> 0; // => -2147483648
2147483649 >> 0; // => -2147483647
```

## Naming Conventions

- 23.2: Use camelCase when naming objects, functions, and instances.

- 23.3: Use PascalCase only when naming constructors or classes.

- 23.5: Don't save references to `this`. Use arrow functions or `Function#bind`.

## Standard Library

- 29.1: Use `Number.isNaN` instead of global `isNaN`.
  - Why? The global isNaN coerces non-numbers to numbers, returning true for anything that coerces to NaN.
  - If this behavior is desired, make it explicit.

- 29.2: Use `Number.isFinite` instead of global `isFinite`.
  - Why? The global isFinite coerces non-numbers to numbers, returning true for anything that coerces to a finite number.
  - If this behavior is desired, make it explicit.

  [1]: https://github.com/airbnb/javascript
