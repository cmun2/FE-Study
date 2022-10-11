# 리액트

## 1

React에서의 상태관리란 데이터에 맞게 적절하게 UX와 UI를 설계하고 구현하는게 상태관리이다.
상태관리가 필요한 이유는 상태관리를 어떻게 하느냐에 따라 의미없는 리렌더 등 성능 이슈를 해결할 수 있고
어떤 상태 라이브러리를 활용하여 어떤구조로 상태관리를 설계해서 다루냐에 따라 유지보수 관점에서 코드의
라이프 사이클이 크게 짧아질수도 길어질수도 있기 때문이다. 먼저 상태관리의 예시를 들면

예를 들어, 인스타그램에서 팔로워수가 많아져서 1억명의 팔로워수가 생겼을때, 1명의 팔로워를 1로 표기하는 것과
1억명의 팔로워를 100000000이라고 표기하기에는 유저입장에서 읽기도 힘들고 너무길어 불필요하게 Box를 많이 차지하는
현상이 발생한다. 이렇게 표기하기에는 1.0억이라고 표기하는게 눈에 더 쉽게 들어오고 UI에 잘 맞다.

이렇게 동적으로 팔로워 상태를 바꾸며 이러한 행동을 팔로워 수 표기의 상태관리라고 한다. 이러한 상태관리는 팔로워 수
뿐만 아니라 댓글이 달려서 하트표시의 댓글이 달린 것이 UI적으로 변한 것을 알 수 있으며 이러한 상태관리는 실시간
상태관리라고 한다. 또한 프로필이 로딩상태일때 잠시 나오는 스피너나 Skeleton UI로 로딩중 표시를 노출 하는 것 또한
로딩상태관리라고 부릅니다. 이러한 상태관리 외에 에러 예외 상황에 대한 상태관리, 로그인한 유저의 권한을 보여주는 상태관리 등
프론트엔드에 쓰이는 상태는 매우 종류가 많고 상태의 조합에 따른 경우의 수를 다 고려해야 한다.

리액트 상태는 이렇게 역할외에도 범위의 측면에서 볼 때 State가 적은 수의 component또는 depth가 깊지 않은 component안에서
영향을 주는 지역상태(local state)또는 많은 컴포넌트와 depth가 깊은 component에 영향을 주는 전역적상태(global state)로 나눌 수 있다.

평소 state관리는 이러한 역할과 범위 측면에 따라 나누어 최소한의 리렌더링 및 페이지 성능을 최대한 끌어올리는 방향으로 관리하고
있습니다.

Reference:

- [프론트엔드의 상태관리란 무엇인가?](https://medium.com/wematch/%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C%EC%9D%98-%EC%83%81%ED%83%9C%EA%B4%80%EB%A6%AC%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-5ff888dab7ad)
- [React state management: What is it and why to use it?](https://www.loginradius.com/blog/engineering/react-state-management/)
- [리액트 상태 관리 가이드](https://www.stevy.dev/react-state-management-guide/)

## 2

Redux는 프론트엔드 상태관리 라이브러리이다. Redux는 웹의 규모가 커지면서 components가 점점 잘게 쪼개지며 한 컴포넌트의 depth
단위가 점점 깊어지면서 부모에서 자식간의 props를 전달하는 과정에서 해당 props가 불필요한 component에서도 전달 받고 보내야 하는
상황인 props drilling 문제와 똑같은 depth level의 자식이 state을 관리할때 props를 서로 전달받을 수 없는 상황에 state을 store라는
제 3자의 공간에서 components들이 필요한 상태를 담아 적절히 필요할 때 언제든지 꺼내고 새로운 state을 업데이트 할 수 있게
도와주는 효과적인 라이브러리이다.

Redux를 항상 써야 하는 건 아니지만 components 단위의 depth가 깊거나 같은 레벨의 depth의 child component에서 props를 전달받아야
하는 상황일 때 쓰면 효과적이다. 또한 리액트에 내장된 Context API로 글로벌상태를 관리할 수 있지만 성능면에서 차이가 난다.
Redux에서는 components에서 글로벌 상태의 특정 값을 의존하게 될 때 해당 값이 바뀔 때에만 리렌더링이 되도록 최적화가 되어있다.
따라서, 글로벌 상태 중 의존하지 않는 값이 바뀌게 될 때에는 컴포넌트에서 낭비 렌더링이 발생하지 않는다.

Reference:

- [리덕스, 어떻게 해야 잘 쓸까](https://ridicorp.com/story/how-to-use-redux-in-ridi/)
- [Redux FAQ: General](https://redux.js.org/faq/general)
- [Redux(리덕스)란?](https://hanamon.kr/redux%EB%9E%80-%EB%A6%AC%EB%8D%95%EC%8A%A4-%EC%83%81%ED%83%9C-%EA%B4%80%EB%A6%AC-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC/)

## 3

Redux외에 여러 상태관리 라이브러리가 있지만 그 중 Recoil에 대한 언급을 하고 싶다. Recoil은 페이스북에서 만든 Context API
기반으로 구현된 함수형 컴포넌트에서만 사용가능한 상태관리 라이브러리이다. Redux는 효과적인 상태관리 라이브러리이지만
너무 많은 보일러 플레이트를 파일마다 반복 작성해야 하는 큰 단점이 있었다. 예를 들어 리덕스 액션과 리듀서들을 도메인마다
분리를 하고 리액트 각 컴포넌트마다 바인딩을 하게 될 시 많은 파일에서 리덕스 코드를 사용하게 되고 많은 양의 보일러 플레이트
코드를 반복해야해서 관리포인트가 많다는 단점이 있었다.

이러한 보일러플레이트를 해결하고 Redux Thunk와 Redux Saga(비동기처리 라이브러리)등 비동기 처리 미들웨어를 추가로 설치하지
않아도 되는 Redux Toolkit이 등장하였지만 아직 recoil에 비해 보일러플레이트가 높으며 recoil은 기존 React의 내장 Hooks사용하는
방식과 유사하며 어플리케이션을 RecoilRoot으로 감싸고 데이터를 atom(작은 단위로 컴포넌트들이 구독할 수 있는 단위)이라는 단위로
선언하여 useState을 Recoil의 useRecoilState으로 대체하는 특징을 가지고 있다.

Recoil의 selector를 활용하여 쉽게 비동기 데이터를 가져올 수 있으며 추가적인 라이브러리 설치가 불필요해 프로젝트 번들이 가벼우며
기존의 Redux의 중앙집중식으로 상태관리가 이루어지며 단방향인 Flux 아미텍처와 달리 저장소 개념보다 작은 상태 단위인 atom이라는
상태 단위로 상태를 관리하여 컴포넌트는 이 atom을 구독하기만 하면 된다는 큰 차이점을 가지고 있다.

- [Recoil Code 예시](./code/recoil.jsx)

<details markdown="1">
<summary>Redux와 Recoil</summary>

<img src="./img/Redux.png" style="width:50%" />
<img src="./img/Recoil.png" style="width:50%" />

</details>

Reference:

- [Redux vs Recoil: which should you use?](https://www.emgoto.com/redux-vs-recoil/)
- [Reducing Boilerplate](https://redux.js.org/usage/reducing-boilerplate)
- [Recoil, 리액트의 상태관리 라이브러리](https://tech.osci.kr/2022/06/16/recoil-state-management-of-react/)

## 4

DOM은 Document Object Model의 약자로 HTML 문서에 있는 모든 node의 구조적 표현이다. DOM은 어플리케이션의 UI를
나타내며 이러한 웹페이지의 UI를 동적으로 변경하려면 DOM 조작이 필요하다. DOM은 스크립트가 문서의 내용, 스타일 및
구조를 업데이트 할 수 있도록 하는 인터페이스이다.

실제 DOM은 논리적 트리가 있는 문서라고 불리며 트리의 각 분기는 노드로 끝나며 각 노드에는 객체가 포함이 된다.
DOM은 트리와 같은 구조로 인해 빠르지만 변경 후에는 업데이트가 된 요소와 자식들을 다시 렌더링하여 어플리케이션
UI를 업데이트해야 하여 UI를 재렌더링시 모든 UI 구성 요소가 느려진다. 모든 DOM 업데이트에 대해 렌더링이 되므로
실제 DOM은 업데이트를 수신하는 특정 항목뿐만이 아닌 전체 목록을 렌더링하게 된다.

이러한 문제를 해결하고자 React에서는 모든 DOM객체에 해당하는 "가상 DOM객체"가 있다. 가상 DOM객체는 실제 DOM객체와
동일한 속성을 갖지만 화면에 있는 내용을 직접 변경할 수는 없다. 가상DOM을 조작하는 것은 화면에 직접 그리지 않기
때문에 실제DOM보다 훨씬 빠르며 React는 우선 모든 단일 가상 DOM을 업데이트하며 이후 가상 DOM이 업데이트 되면 그
전 가상 DOM과 비교하여 어떤 가상 DOM 요소가 변경되었는지 알아내며 해당 요소만 업데이트 하게 하는 "diffing"이라는
프로세스를 실행합니다.

Reference:

- [The Document Object Model](https://eloquentjavascript.net/14_dom.html)
- [React: The Virtual DOM](https://www.codecademy.com/article/react-virtual-dom)
- [Difference between Virtual DOM and Real DOM](https://www.geeksforgeeks.org/differnece-between-virtual-dom-and-real-dom/)

<details markdown="1">
<summary>실제DOM과 가상DOM 원리(React)</summary>

<img src="./img/DOM.png" style="width:50%" />
<img src="./img/VirtualDOM.jpeg" style="width:50%" />

</details>
