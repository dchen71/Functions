class CreateAlbums < ActiveRecord::Migration
  def change
    create_table :albums do |t|
      t.string :cover
      t.string :title
      t.string :artist

      t.timestamps null: false
    end
  end
end
