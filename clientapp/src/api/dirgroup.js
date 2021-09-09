import {HTTP} from './common'

export class DirGroup {
  static list() {
    return HTTP.get('/dirgroup/').then(response => {
      return response.data
    })
  }

  static applySelected(directions) {
    return HTTP.post(`/dirgroupselection/`, directions).then(response => {
      return response
    })
  }

  static getSelected(dirGroup) {
    return !dirGroup.directions.some(dir => !dir.selected)
  }

  static selectGroup(dirGroup) {
    for (let dir of dirGroup.directions) {
      dir.selected = dirGroup.selected
    }
  }

  static selectDir(dirGroup) {
    for (const dir of dirGroup.directions) {
      if (!dir.selected) {
        dirGroup.selected = false
        return
      }
    }
    dirGroup.selected = true
  }
}
