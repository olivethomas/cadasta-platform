import { combineReducers } from 'redux';
import user from './account/reducer';
import messages from './messages/reducer';

const reducer = combineReducers({
  user,
  messages,
});

export default reducer;
